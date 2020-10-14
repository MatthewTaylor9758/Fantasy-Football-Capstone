import React from 'react';
import { NavLink } from 'react-router-dom';
import { makeStyles, Container, TextField, Button, Typography, AppBar, Toolbar } from '@material-ui/core';

function NavBar() {
  const useStyles = makeStyles({
    navBar: {
      backgroundImage: 'radial-gradient(rgba(110, 12, 25, .9), rgb(110, 12, 25, .9), rgba(0, 0, 0, .7))',
      width: '100vw',
      padding: '0'
    }
  })

  const classes = useStyles();

  return (
    <>
      <AppBar position='sticky' className={classes.navBar}>
        <Toolbar>
          <Typography>This is just a test of something to look at</Typography>
        </Toolbar>
      </AppBar>
    </>
  )
}

// rgb(110, 12, 25)
export default NavBar;
