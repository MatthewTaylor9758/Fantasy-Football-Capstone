import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { NavLink } from 'react-router-dom';
import { makeStyles, Container, TextField, Button, Typography } from '@material-ui/core';
import NavBar from '../components/NavBar';

function MyTeamPage() {
  const dispatch = useDispatch();

  const handleGetPlayers = (e) => {

  }

  return (
    <>
      <NavBar />
      <Container>
        <Typography variant='h1'>This is the My Team Page</Typography>
        <Button onClick={handleGetPlayers}>Show My Teams</Button>
      </Container>
    </>
  )
}

export default MyTeamPage;
