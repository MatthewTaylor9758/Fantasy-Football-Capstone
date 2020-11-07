import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { NavLink } from 'react-router-dom';
import { makeStyles, Container, TextField, Button, Typography, Grid, AppBar, Modal } from '@material-ui/core';
import Cookies from 'js-cookie';
import NavBar from '../components/NavBar';
import '../styles/titleBar.css';
import { new_ffsplayer } from '../store/ffsplayers';

function AvailPlayers() {
  const dispatch = useDispatch()
  const myTeam = Object.values(useSelector(state => state.ffsplayers))
  const myTeamId = useSelector(state => state.teams.id)
  const myLeagueId = useSelector(state => state.leagues.id)
  const ffsplayers = useSelector(state => state.ffsplayers);
  const [players, updatePlayers] = useState([])
  const [open, setOpen] = useState(false);
  const [specificPlayers, updateSpecificPlayers] = useState('');
  const [player, setPlayer] = useState('');
  const csrfToken = Cookies.get('XSRF-TOKEN');
  const handleShowAllPlayers = async (e) => {
    console.log(csrfToken);
    console.log(myLeagueId);
    if (myLeagueId) {
      const res = await fetch(`/api/players/${myLeagueId}`);
      const data = await res.json();
      console.log(data.players);
      updatePlayers(data.players);
      players.length ? console.log(true) : console.log(false)
    }
  }

  const handleShowSpecificPlayers = async (e) => {
    console.log(e.target.value)
    const res = await fetch(`/api/players/${myLeagueId}/${e.target.value}`);
    e.persist()
    const data = await res.json();
    console.log(data.players);
    updatePlayers(data.players);
  }

  useEffect(() => {
    handleShowAllPlayers()
  }, [])

  // let playerSelect = '';

  useEffect((e) => {
    // console.log(playerSelect)
    handleShowAllPlayers();
  }, [ffsplayers])

  // useEffect(() => {
  //   handleShowSpecificPlayers()
  // }, [players])

  const handleAddPlayer = async (e) => {
    console.log(e.target.value, myTeamId, myLeagueId);
    const res = await dispatch(new_ffsplayer(e.target.value, myLeagueId, myTeamId))
    // console.log(playerSelect)
  }

  const handleOpen = (e) => {
    console.log(e.target.value)
    setPlayer(e.target.value);
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  const useStyles = makeStyles((theme) => ({
    playerInfo: {
      position: 'relative',
      // background: 'linear-gradient(-45deg, rgba(255, 255, 255, .2), rgba(25, 111, 12, .7))',
    },
    playersContainer: {
      width: '85%',
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
      backgroundColor: 'rgba(255, 255, 255, .6)',
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
      border: '1px solid black',
      height: '3em'
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
      alignItems: 'center',
      fontWeight: '450'
    },
    playerTitleName: {
      display: 'flex',
      alignItems: 'center',
      fontWeight: '450'
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
      backgroundColor: 'rgba(255, 255, 255, .6)',
      paddingTop: '1em',
      paddingBottom: '1em',
      borderRadius: '3px',
      marginRight: '5px',

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
      justifyContent: 'center',
    },
    positionSelector: {
      display: 'flex',
      justifyContent: 'center',
      marginBottom: '.8em',
      background: 'rgba(255, 255, 255, .3)',
      padding: '.5em 1em',
      borderRadius: '8px'
    },
    addButton: {
      border: '1px solid rgb(0, 0, 200)',
      borderRadius: '4px',
      padding: '.3em',
      fontFamily: 'Roboto, Helvetica, Arial, sans-serif',
      fontWeight: '500',
      color: 'rgb(0, 0, 200)',
      backgroundColor: 'transparent',
      textTransform: 'uppercase',
      '&:hover': {
        backgroundColor: 'rgba(0, 0, 200, .3)',
        color: 'white'
      }
    },
    positionButton: {
      border: '1px solid rgb(0, 0, 0)',
      borderRadius: '4px',
      padding: '.3em',
      margin: '0 .7em',
      fontFamily: 'Roboto, Helvetica, Arial, sans-serif',
      fontWeight: '500',
      color: 'rgb(0, 0, 0)',
      backgroundColor: 'transparent',
      textTransform: 'uppercase',
      '&:hover': {
        backgroundColor: 'rgba(0, 0, 0, .3)',
        color: 'white'
      }
    },
    noLeagueDiv: {
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
      minHeight: 'calc(100vh - 64px)',
      minWidth: '100vw',
      // backgroundColor: 'rgba(255, 255, 255, .3)',
    },
    playerNameButton: {
      background: 'transparent',
      border: 'none',
      outline: 'none',
      '&:hover': {
        cursor: 'pointer'
      }
    },
    modalContainer: {
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
      height: '100vh'
    },
    playerInfoModal: {
      width: '65%',
      height: '75%',
      backgroundColor: 'rgba(255, 255, 255, .9)',
      color: 'black',
      margin: '0'
    }
  }))

  const classes = useStyles();

  return (
    <>
      <NavBar />
      {myLeagueId ?
        <>
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
                      <button value='QB' className={classes.positionButton} onClick={handleShowSpecificPlayers}>
                        QB
                  </button>
                      <button value='RB' className={classes.positionButton} onClick={handleShowSpecificPlayers}>
                        RB
                  </button>
                      <button value='WR' className={classes.positionButton} onClick={handleShowSpecificPlayers}>
                        WR
                  </button>
                      <button value='TE' className={classes.positionButton} onClick={handleShowSpecificPlayers}>
                        TE
                  </button>
                      <button value='K' className={classes.positionButton} onClick={handleShowSpecificPlayers}>
                        K
                  </button>
                      <button value='DEF' className={classes.positionButton} onClick={handleShowSpecificPlayers}>
                        DEF
                  </button>
                    </div>
                    {players.map(player => {
                      return (
                        <Grid container item className={classes.playerRow}>
                          <Grid item xs={2} className={classes.playerTitleName}>
                            <button value={player['full_name']} onClick={handleOpen} className={classes.playerNameButton}>
                              {player['full_name']}
                            </button>
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
                          <Grid item xs={1} className={classes.playerTitle}>
                            <button className={classes.addButton} value={player['player_id']} onClick={handleAddPlayer}>Add</button>
                          </Grid>
                        </Grid>
                      )
                    })
                    }
                  </Container>
                  : null}
                <Modal
                  open={open}
                  onClose={handleClose}
                  aria-labelledby="simple-modal-title"
                  aria-describedby="simple-modal-description"
                >
                  <div className={classes.modalContainer}>
                    <div className={classes.playerInfoModal}>
                      This is just a test for the modal. {player}
                    </div>
                  </div>
                </Modal>
              </Grid>
            </Grid>
          </Container>
        </>
        :
        <div id='noLeagueDiv' className={classes.noLeagueDiv}>
          <Typography variant='h3'>You must join a league to have available players.</Typography>
        </div>
      }
    </>
  )
}

export default AvailPlayers;
