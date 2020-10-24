import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { NavLink } from 'react-router-dom';
import { makeStyles, Container, TextField, Button, Typography, Grid } from '@material-ui/core';
import Cookies from 'js-cookie';

function AvailPlayers() {
  const dispatch = useDispatch()
  const [players, updatePlayers] = useState([])
  const csrfToken = Cookies.get('XSRF-TOKEN');
  const handleShowAllPlayers = async (e) => {
    console.log(csrfToken);
    const res = await fetch('/api/players');
    const data = await res.json();
    console.log(data.players);
    updatePlayers(data.players);
    debugger
    players.length ? console.log(true) : console.log(false)
  }

  useEffect(() => {
    handleShowAllPlayers()
  }, [])

  const useStyles = makeStyles((theme) => ({
    playersContainer: {
      width: '100%',
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center'
    },
    playerRow: {
      display: 'flex',
      justifyContent: 'center'
    }
  }))

  const classes = useStyles();

  return (
    <>
      <Typography variant='h1'>This is the Available Players page</Typography>
      <Button onClick={handleShowAllPlayers}>Show Available Players</Button>
      {players.length ?
        <Container className={classes.playersContainer}>
              {players.map(player => {
                  return (
                    <Grid container item className={classes.playerRow}>
                      <Grid item xs={2}>
                        {player['full_name']}
                      </Grid>
                      <Grid item xs={1}>
                        {player['nfl_team']}
                      </Grid>
                      <Grid item xs={1}>
                        {player['position']}
                      </Grid>
                      <Grid item xs={1}>
                        {player['height']}
                      </Grid>
                      <Grid item xs={1}>
                        {player['weight']}
                      </Grid>
                      <Grid item xs={2}>
                        {player['dob']}
                      </Grid>
                      <Grid item xs={2}>
                        {player['college']}
                      </Grid>
                    </Grid>
                  )
                })
          }
        </Container>
      : null}
    </>
  )
}

export default AvailPlayers;
