import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { NavLink } from 'react-router-dom';
import { makeStyles, Container, TextField, Button, Typography, Grid, AppBar } from '@material-ui/core';
import Cookies from 'js-cookie';
import NavBar from '../components/NavBar';
import '../styles/titleBar.css';
function AvailPlayers() {
  const dispatch = useDispatch()
  const myTeam = Object.values(useSelector(state => state.ffsplayers))
  const [players, updatePlayers] = useState([])
  const csrfToken = Cookies.get('XSRF-TOKEN');
  const handleShowAllPlayers = async (e) => {
    console.log(csrfToken);
    const res = await fetch('/api/players');
    const data = await res.json();
    console.log(data.players);
    updatePlayers(data.players);
    players.length ? console.log(true) : console.log(false)
  }

  const handleShowSpecificPlayers = async (e) => {
    console.log(e.target.value)
    const res = await fetch(`/api/players/${e.target.value}`);
    const data = await res.json();
    console.log(data.players);
    updatePlayers(data.players);
  }

  useEffect(() => {
    handleShowAllPlayers()
  }, [])

  // useEffect(() => {
  //   handleShowSpecificPlayers()
  // }, [players])

  const handleAddPlayer = (e) => {

  }

  const useStyles = makeStyles((theme) => ({
    playerInfo: {
      position: 'relative',
      background: 'linear-gradient(-45deg, rgba(255, 255, 255, .2), rgba(25, 111, 12, .7))',
    },
    playersContainer: {
      width: '85%',
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
      backgroundColor: 'rgba(255, 255, 255, .35)',
      paddingTop: '1em',
      borderRadius: '3px'
    },
    playersContainerBar: {
      width: '85%',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center'
    },
    playerRow: {
      display: 'flex',
      justifyContent: 'center',
      padding: '.2em 0',
      border: '1px solid black'
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
    playerTitle: {
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center'
    },
    playerTitleName: {
      display: 'flex',
      alignItems: 'center'
    },
    secondBar: {
      display: 'flex',
      justifyContent: 'center',
    },
    secondBarPlayer: {
      display: 'flex',
      justifyContent: 'center',
      width: '85%'
    },
    myTeamContainer: {
      display: 'flex',
      flexDirection: 'column',
      backgroundColor: 'rgba(255, 255, 255, .35)',
      paddingTop: '1em',
      paddingBottom: '1em',
      borderRadius: '3px'
    },
    leftGrid: {
      position: 'sticky',
      overflowY: 'overlay',
      height: 'calc(100vh - 95px)'
    },
    rightGrid: {
      overflowY: 'overlay',
      height: 'calc(100vh - 95px)'
    },
    myTeamInfo: {
      display: 'flex',
      justifyContent: 'space-between',
      width: '100%'
    },
    myTeamPlayer: {
      display: 'flex',
      maxWidth: '33.3%',
      justifyContent: 'center',
      padding: '.3em'
    },
    myTeamPlayerName: {
      display: 'flex',
      maxWidth: '33.3%',
      justifyContent: 'center',
      padding: '.3em 0'
    },
    myTeamPlayerPosition: {
      display: 'flex',
      maxWidth: '33.3%',
      justifyContent: 'flex-start',
      padding: '.3em'
    },
    myTeamTitle: {
      display: 'flex',
      justifyContent: 'center'
    },
    positionSelector: {
      display: 'flex',
      justifyContent: 'center',
      marginBottom: '.8em',
      background: 'rgba(255, 255, 255, .5)',
      padding: '.2em 0',
      borderRadius: '8px'
    }
  }))

  const classes = useStyles();

  return (
    <>
      <NavBar />

      <AppBar id='secondBar'>
          <Grid container item className={classes.secondBar}>
            <Grid item xs={2}>
              <Grid item className={classes.myTeamTitle}>
                My Team
              </Grid>
            </Grid>
            <Grid xs={10} className={classes.secondBarPlayer}>
              <Container className={classes.playersContainerBar}>
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
                <Grid item xs={2} className={classes.gridTitleName}>
                  College
                </Grid>
                <Grid item xs={1}>

                </Grid>
              </Container>
            </Grid>
          </Grid>
      </AppBar>
      <Container className={classes.playerInfo}>
        <Grid container xs={12}>
          <Grid xs={2} className={classes.leftGrid}>
            <div className={classes.myTeamContainer}>
              {myTeam.map(player => {
                return (
                  <Grid container className={classes.myTeamInfo}>
                    <Grid item xs={1}>

                    </Grid>
                    <Grid item xs={4} className={classes.myTeamPlayerName}>
                      {player.full_name}
                    </Grid>
                    <Grid item xs={3} className={classes.myTeamPlayer}>
                      {player.nfl_team}
                    </Grid>
                    <Grid item xs={3} className={classes.myTeamPlayerPosition}>
                      {player.position}
                    </Grid>
                  </Grid>
                )
              })}
            </div>
          </Grid>
          <Grid xs={10} className={classes.rightGrid}>
            {players.length ?
              <Container className={classes.playersContainer}>
                <div className={classes.positionSelector}>
                  <button value='QB' onClick={handleShowSpecificPlayers}>
                    QB
                  </button>
                  <button value='RB' onClick={handleShowSpecificPlayers}>
                    RB
                  </button>
                  <button value='WR' onClick={handleShowSpecificPlayers}>
                    WR
                  </button>
                  <button value='TE' onClick={handleShowSpecificPlayers}>
                    TE
                  </button>
                  <button value='K' onClick={handleShowSpecificPlayers}>
                    K
                  </button>
                  <button value='DEF' onClick={handleShowSpecificPlayers}>
                    DEF
                  </button>
                </div>
                {players.map(player => {
                  return (
                    <Grid container item className={classes.playerRow}>
                      <Grid item xs={2} className={classes.playerTitleName}>
                        {player['full_name']}
                      </Grid>
                      <Grid item xs={1} className={classes.playerTitle}>
                        {player['nfl_team']}
                      </Grid>
                      <Grid item xs={1} className={classes.playerTitle}>
                        {player['position']}
                      </Grid>
                      <Grid item xs={1} className={classes.playerTitle}>
                        {player['height']}
                      </Grid>
                      <Grid item xs={1} className={classes.playerTitle}>
                        {player['weight']}
                      </Grid>
                      <Grid item xs={2} className={classes.playerTitle}>
                        {player['dob']}
                      </Grid>
                      <Grid item xs={2} className={classes.playerTitleName}>
                        {player['college']}
                      </Grid>
                      <Grid item xs={1}>
                        <Button onClick={handleAddPlayer}>Add</Button>
                      </Grid>
                    </Grid>
                  )
                })
                }
              </Container>
              : null}
          </Grid>
        </Grid>
      </Container>
    </>
  )
}

export default AvailPlayers;
