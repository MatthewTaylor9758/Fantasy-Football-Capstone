import React from 'react';
import { NavLink } from 'react-router-dom';
import { makeStyles, Typography, AppBar, Toolbar, Grid } from '@material-ui/core';

function Footer() {

  const useStyles = makeStyles({
    footer: {
      bottom: '0',
    }
  })

  const classes = useStyles();

  return (
    <>
      <AppBar position='sticky' className={classes.footer}>
        <Toolbar>
          This is just a test for the footer position.
        </Toolbar>
      </AppBar>
    </>
  )
}

export default Footer;
