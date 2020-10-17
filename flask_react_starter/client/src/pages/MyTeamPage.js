import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { NavLink } from 'react-router-dom';
import { getTeam } from '../store/teams';
import { getLeague } from '../store/leagues';
import { get_ffsplayer } from '../store/ffsplayers';
import { makeStyles, Container, TextField, Button, Typography } from '@material-ui/core';
import NavBar from '../components/NavBar';

function MyTeamPage() {
  const dispatch = useDispatch();
  const user = useSelector(state => state.auth);
  const team = useSelector(state => state.teams);
  // let team_ffsplayers = JSON.parse(localStorage.getItem('ffsplayers'));
  // const [teamFfsplayersObj, setTeamFfsplayersObj] = useState(team_ffsplayers ? team_ffsplayers : {})
  const ffsplayers = useSelector(state => state.ffsplayers)
  const [userTeam, setUserTeam] = useState('');
  const userId = user.id;
  const teamLeagueId = team.league_id;


  const handleGetPlayers = async (e) => {
    const res = await dispatch(get_ffsplayer(team.id, teamLeagueId))
    console.log(res);
  }

  const handleGetLeague = async (e) => {
    console.log(teamLeagueId);
    const res = await dispatch(getLeague(teamLeagueId));
    console.log(res);
  }

  const handleJoinLeague = (e) => {

  }

  const handleGetTeam = async (e) => {
    console.log(userId)
    const res = await dispatch(getTeam(userId))
    // console.log(res)
    // await setUserTeam(res['team'])
    // console.log(userTeam)
    // console.log(teamLeagueId);
    // const res2 = await dispatch(getLeague(teamLeagueId));
    // const res3 = await dispatch(get_ffsplayer(team.id, teamLeagueId))
    console.log(res)
    // console.log(res2)
    // console.log(res3)
    // debugger
  }
  let playerArr = [...Object.values(ffsplayers)]

  useEffect(() => {
    // console.log(team_ffsplayers)
    handleGetTeam();
  }, [])

  // const testing = () => {
  //   console.log(playerArr)
  //   console.log(Object.values(...Object.values(ffsplayers)))
  // }


  return (
    <>
      <NavBar />
      <Container>
        <Typography variant='h1'>This is the My Team Page</Typography>
        <Button onClick={handleGetPlayers}>Show My Teams</Button>
        <Button onClick={handleGetLeague}>Get League</Button>
        <Button onClick={handleJoinLeague}>Join League</Button>
        <Button onClick={handleGetTeam}>Get Team</Button>
        {/* <Button onClick={testing}>Test</Button> */}
        <div>
          {playerArr ? playerArr.map(player => {
            return (
              <div>
                {Object.values(player)}
              </div>
            )
          }) : null}
        </div>
      </Container>
    </>
  )
}

export default MyTeamPage;
