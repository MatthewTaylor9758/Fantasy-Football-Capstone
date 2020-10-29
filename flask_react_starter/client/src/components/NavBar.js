import React from 'react';
import { NavLink } from 'react-router-dom';
import { useSelector } from 'react-redux';
import { makeStyles, Container, TextField, Button, Typography, AppBar, Toolbar, Grid } from '@material-ui/core';
import '../styles/navBar.css';

function NavBar() {
  const user = useSelector(state => state.auth);

  const logout = () => {
    localStorage.clear()
    window.location.href = '/login'
  }

  const useStyles = makeStyles({
    navBar: {
      backgroundImage: 'radial-gradient(rgba(110, 12, 25, .9), rgb(110, 12, 25, .9), rgba(0, 0, 0, .7))',
      width: '100%',
      padding: '0',
      maxHeight: '64px'
    },
    leftSide: {
      display: 'flex',
      padding: '0 2em',
      justifyContent: 'flex-start',
    },
    middle: {
      display: 'flex',
      justifyContent: 'center',
    },
    rightSide: {
      display: 'flex',
      padding: '0 2em',
      justifyContent: 'flex-end',
    },
    sideLinks: {
      padding: '0 .5em'
    },
    logo: {
      fontFamily: 'Roboto'
    },
    logoutButton: {
      padding: '0 .5em',
      '&:hover': {
        cursor: 'pointer'
      }
    }
  })

  const classes = useStyles();

  return (
    <>
      <AppBar position='sticky' className={classes.navBar}>
        <Toolbar>
          <Grid container xs={12}>
            <Grid item xs={3} className={classes.leftSide}>
              {localStorage.getItem('user') ?
                <div>
                  <NavLink to={`/myTeam/${user.id}`} id='links' className={classes.sideLinks}>My team</NavLink>
                  <NavLink to='/players' id='links' className={classes.sideLinks}>Available Players</NavLink>
                </div>
              : null}
            </Grid>
            <Grid item xs={6} className={classes.middle}>
              <NavLink to="/" activeclass="active" id='links'className={classes.logo}>FFStockpile</NavLink>
            </Grid>
            <Grid item xs={3} className={classes.rightSide}>
              {!localStorage.getItem('user') ?
                <div>
                  <NavLink to='/login' id='links' className={classes.sideLinks}>Login</NavLink>
                  <NavLink to='/signup' id='links' className={classes.sideLinks}>Sign up</NavLink>
                </div>
              :
                <div className={classes.logoutDiv}>
                  <a onClick={logout} className={classes.logoutButton}>Log out</a>
                </div>
              }
            </Grid>
          </Grid>
        </Toolbar>
      </AppBar>
    </>
  )
}

// rgb(110, 12, 25)
export default NavBar;
