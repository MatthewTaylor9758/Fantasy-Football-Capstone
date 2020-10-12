import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { NavLink } from 'react-router-dom';
import { makeStyles, Container, TextField, Button, Typography } from '@material-ui/core';

function AvailPlayers() {
  const dispatch = useDispatch()

  const handleShowAllPlayers = (e) => {

  }

  return (
    <>
      <Typography variant='h1'>This is the Available Players page</Typography>
      <Button onClick={handleShowAllPlayers}>Show Available Players</Button>
    </>
  )
}

export default AvailPlayers;
