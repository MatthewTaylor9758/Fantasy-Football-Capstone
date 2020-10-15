import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { NavLink } from 'react-router-dom';
import { getTeam } from '../store/teams';
import { getLeague } from '../store/leagues';
import { makeStyles, Container, TextField, Button, Typography } from '@material-ui/core';
import NavBar from '../components/NavBar';

function MyTeamPage() {
  const dispatch = useDispatch();
  const user = useSelector(state => state.auth);
  const team = useSelector(state => state.teams);
  const [userTeam, setUserTeam] = useState('');
  const userId = user.id;
  const teamLeagueId = team.league_id;

  const handleGetPlayers = (e) => {

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
    console.log(res)
    debugger
  }

  return (
    <>
      <NavBar />
      <Container>
        <Typography variant='h1'>This is the My Team Page</Typography>
        <Button onClick={handleGetPlayers}>Show My Teams</Button>
        <Button onClick={handleGetLeague}>Get League</Button>
        <Button onClick={handleJoinLeague}>Join League</Button>
        <Button onClick={handleGetTeam}>Get Team</Button>
      </Container>
    </>
  )
}

export default MyTeamPage;
