import React, { useEffect, useState } from 'react';
import { NavLink } from 'react-router-dom';
import { useSelector } from 'react-redux';
import { makeStyles, Container, TextField, Button, Typography } from '@material-ui/core';
import NavBar from '../components/NavBar';

function SplashPage() {
  const useStyles = makeStyles({
    outerContainer: {
      backgroundImage: 'linear-gradient(to top, rgba(255, 255, 255, .2), rgba(25, 111, 12, .7))',
      height: '100vh',
      width: '100vw',
    }
  })
  const classes = useStyles();

  return (
    <>
      <NavBar />
      <Container className={classes.outerContainer}>
        <Typography variant='h1'>This is the Splash Page</Typography>
        <nav>
          <ul>
            <li><NavLink to="/" activeclass="active">Home</NavLink></li>
            <li><NavLink to="/users" activeclass="active">Users</NavLink></li>
            <li><NavLink to='/login'>Login</NavLink></li>
            <li><NavLink to='/signup'>Sign up</NavLink></li>
            <li><NavLink to='/myTeam/:id'>My team</NavLink></li>
            <li><NavLink to='/players'>Available Players</NavLink></li>
          </ul>
        </nav>
      </Container>
    </>
  )
}

export default SplashPage;
