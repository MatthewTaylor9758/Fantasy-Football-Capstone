import React from 'react';
import { NavLink } from 'react-router-dom';
import { makeStyles, Typography, AppBarr, Toolbar, Grid } from '@material-ui/core';

function Footer() {
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
