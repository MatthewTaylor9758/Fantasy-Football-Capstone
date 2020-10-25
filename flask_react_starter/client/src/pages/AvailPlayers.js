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

  useEffect(() => {
    handleShowAllPlayers()
  }, [])

  const handleAddPlayer = (e) => {

  }

  const useStyles = makeStyles((theme) => ({
    playerInfo: {
      position: 'relative',
    },
    playersContainer: {
      width: '85%',
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center'
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
    },
    leftGrid: {
      position: 'sticky'
    },
    rightGrid: {
      overflowY: 'overlay',
      height: 'calc(100vh - 95px)'
    }
  }))

  const classes = useStyles();

  return (
    <>
      <NavBar />

      <AppBar id='secondBar'>
          <Grid container item className={classes.secondBar}>
            <Grid item xs={2}>
              <Grid item>
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
                  <div>
                    {player.full_name}
                  </div>
                )
              })}
            </div>
          </Grid>
          <Grid xs={10} className={classes.rightGrid}>
            {players.length ?
              <Container className={classes.playersContainer}>
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
