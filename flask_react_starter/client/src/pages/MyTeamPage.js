import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { NavLink, Redirect } from 'react-router-dom';
import { getTeam } from '../store/teams';
import { getLeague } from '../store/leagues';
import { get_ffsplayer, remove_ffsplayer } from '../store/ffsplayers';
import { makeStyles, Container, TextField, Button, Typography, Grid } from '@material-ui/core';
import NavBar from '../components/NavBar';
import '../styles/teamPage.css';
import Footer from '../components/Footer';

function MyTeamPage() {
  const dispatch = useDispatch();
  const user = useSelector(state => state.auth);
  const team = useSelector(state => state.teams);
  const leagueName = useSelector(state => state.leagues.name);
  const teamName = useSelector(state => state.teams.name);
  // let team_ffsplayers = JSON.parse(localStorage.getItem('ffsplayers'));
  // const [teamFfsplayersObj, setTeamFfsplayersObj] = useState(team_ffsplayers ? team_ffsplayers : {})
  const ffsplayers = useSelector(state => state.ffsplayers)
  const [userTeam, setUserTeam] = useState('');
  const userId = user.id;
  const teamLeagueId = team.league_id;

  if (!user) {
    window.location.href = '/';
  }


  const handleGetPlayers = async (e) => {
    const res = await dispatch(get_ffsplayer(teamLeagueId, team.id))
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
    // debugger
    const res = await dispatch(getTeam(userId))
    // console.log(res)
    // await setUserTeam(res['team'])
    // console.log(userTeam)
    // console.log(teamLeagueId);
    // const res2 = await dispatch(getLeague(teamLeagueId));
    // const res3 = await dispatch(get_ffsplayer(team.id, teamLeagueId))
    console.log(res);
    console.log(playerArr);
    // console.log(res2)
    // console.log(res3)
    // debugger
  }
  let playerArr = [...Object.values(ffsplayers)]

  useEffect(() => {
    // console.log(team_ffsplayers)
    handleGetTeam();
    console.log(playerArr)
  }, [])

  // const testing = () => {
  //   console.log(playerArr)
  //   console.log(Object.values(...Object.values(ffsplayers)))
  // }



  const handleRemovePlayer = async (e) => {
    console.log(e.target.value);
    const res = await dispatch(remove_ffsplayer(e.target.value, teamLeagueId));
    handleGetPlayers(team.id, teamLeagueId)
  }

  const useStyles = makeStyles((theme) => ({
    // columns: {
    //   display: 'flex',
    //   justifyContent: 'space-between',
    //   width: '100%'
    // },
    outsideLinks: {
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      borderRight: '2px solid gray',
      height: '100%'
    },
    outsideContainer: {
      // background: 'linear-gradient(-45deg, rgba(255, 255, 255, .2), rgba(25, 111, 12, .7))',
      height: '100%'
    },
    infoContainer: {
      position: 'absolute',
      top: '100px',
      minWidth: 'fit-content',
    },
    playerInfo: {
      display: 'flex',
      justifyContent: 'center',
      height: 'fit-content',
      minWidth: 'fit-content',
      marginLeft: '5em',
      // overflowY: 'scroll'
      // backgroundColor: 'rgba(255, 255, 255, .55)',
    },
    logoutDiv: {
      width: '100%',
      display: 'flex',
      justifyContent: 'flex-end'
    },
    logoutButton: {
      '&:hover': {
        backgroundColor: 'rgb(200, 0, 0)'
      }
    },
    gridTitle: {
      display: 'flex',
      justifyContent: 'center',
      minWidth: 'fit-content',
      fontWeight: '600'
    },
    gridTitleName: {
      display: 'flex',
      minWidth: 'fit-content',
      fontWeight: '600'
    },
    playerInfoContainer: {
      paddingLeft: '0',
      paddingTop: '.5em',
      width: '100%',
      overflowY: 'overlay'
    },
    playerItem: {
      display: 'flex',
      justifyContent: 'center'
    },
    linksContainer: {
      height: '100%',
      // backgroundColor: 'rgba(255, 255, 255, .55)',
    },
    stuffContainer: {
      height: '100%',
      backgroundColor: 'rgba(255, 255, 255, .6)',
      padding: '1em',
      borderRadius: '10px'
    },
    helpLinks: {
      marginTop: '.5em',
      textDecoration: 'none'
    },
    playerData: {
      display: 'flex',
      justifyContent: 'center',
      border: '1px solid black',
      padding: '.2em 0',
      backgroundColor: 'rgba(255, 255, 255, .5)',
      height: '2.5em',
      display: 'flex',
      alignItems: 'center'
    },
    playerDataName: {
      border: '1px solid black',
      padding: '0 0 0 .2em',
      backgroundColor: 'rgba(255, 255, 255, .5)',
      height: '2.5em',
      display: 'flex',
      alignItems: 'center'
    },
    teamInfoContainer: {
      display: 'flex',
      flexDirection: 'column',
      justifyContent: 'center',
      alignItems: 'center'
    },
    leagueAndTeam: {
      display: 'flex',
      flexDirection: 'column',
      justifyContent: 'center',
      alignItems: 'center',
      marginBottom: '1.5em',
      border: '2px solid black'
    },
    leagueAndTeamInfo: {
      padding: '.2em'
    },
    dropButton: {
      border: '1px solid rgb(200, 0, 78)',
      borderRadius: '4px',
      padding: '.3em',
      fontFamily: 'Roboto, Helvetica, Arial, sans-serif',
      fontWeight: '500',
      color: 'rgb(200, 0, 78)',
      backgroundColor: 'transparent',
      textTransform: 'uppercase',
      '&:hover': {
        backgroundColor: 'rgba(200, 0, 0, .3)',
        color: 'black',
        cursor: 'pointer',
      }
    },
    noPlayers: {
      marginTop: '.5em'
    }
  }))

  const classes = useStyles()

  return (
    <>
      {user ?
        <div id='bodyDiv'>
          <NavBar />
          <div className={classes.outsideContainer}>
            <Container className={classes.infoContainer} maxWidth={false}>
              <Grid container item xs={12} className={classes.stuffContainer}>
                <Container className={classes.leagueAndTeam}>
                  <Typography variant='h4' className={classes.leagueAndTeamInfo}>League: {leagueName}</Typography>
                  <Typography variant='h4' className={classes.leagueAndTeamInfo}>Team: {teamName}</Typography>
                </Container>
                <Grid item xs={2} className={classes.linksContainer}>
                  <div className={classes.outsideLinks}>
                    <a href='https://fantasy.nfl.com/' target='_blank' className={classes.helpLinks}>NFL Fantasy</a>
                    <a href='https://www.cbssports.com/fantasy/' target='_blank' className={classes.helpLinks}>CBS Fantasy</a>
                    <a href='https://www.espn.com/fantasy/football/' target='_blank' className={classes.helpLinks}>ESPN Fantasy</a>
                    <a href='https://football.fantasysports.yahoo.com/' target='_blank' className={classes.helpLinks}>Yahoo Fantasy</a>
                  </div>
                </Grid>
                <Grid container item xs={9} className={classes.playerInfo}>

                  <Grid container item>
                    <Grid item xs={2} className={classes.gridTitleName}>
                      Name
                          </Grid>
                    <Grid item xs={1} className={classes.gridTitle}>
                      Team
                          </Grid>
                    <Grid item xs={1} className={classes.gridTitle}>
                      Position
                          </Grid>
                    <Grid item xs={1} className={classes.gridTitle}>
                      Height
                          </Grid>
                    <Grid item xs={1} className={classes.gridTitle}>
                      Weight
                          </Grid>
                    <Grid item xs={2} className={classes.gridTitle}>
                      DOB
                          </Grid>
                    <Grid item xs={2} className={classes.gridTitle}>
                      College
                          </Grid>
                    <Grid item xs={1} className={classes.gridTitle}>

                    </Grid>
                  </Grid>
                  <Grid className={classes.playerInfoContainer}>
                    {playerArr.length ? playerArr.map(player => {
                      return (
                        <Grid container item>
                          <Grid item xs={2} className={classes.playerDataName}>
                            {player['full_name']}
                          </Grid>
                          <Grid item xs={1} className={classes.playerData}>
                            {player['nfl_team']}
                          </Grid>
                          <Grid item xs={1} className={classes.playerData}>
                            {player['position']}
                          </Grid>
                          <Grid item xs={1} className={classes.playerData}>
                            {player['height']}
                          </Grid>
                          <Grid item xs={1} className={classes.playerData}>
                            {player['weight']}
                          </Grid>
                          <Grid item xs={2} className={classes.playerData}>
                            {player['dob']}
                          </Grid>
                          <Grid item xs={2} className={classes.playerData}>
                            {player['college']}
                          </Grid>
                          <Grid item xs={1} className={classes.playerData}>
                            <button className={classes.dropButton} value={player['player_id']} onClick={handleRemovePlayer}>Drop</button>
                          </Grid>
                        </Grid>
                      )
                    }) :
                    <Typography variant='h5' className={classes.noPlayers}> - You must have a team to have players.</Typography>
                    }
                  </Grid>

                </Grid>

              </Grid>
            </Container>
          </div>
        </div>
      : <Redirect to='/' />}
    </>
  )
}

export default MyTeamPage;
