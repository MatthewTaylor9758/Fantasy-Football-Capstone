import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { NavLink } from 'react-router-dom';
import { makeStyles, Container, TextField, Button, Typography } from '@material-ui/core';
import Cookies from 'js-cookie';

function AvailPlayers() {
  const dispatch = useDispatch()
  const players = [];
  const csrfToken = Cookies.get('XSRF-TOKEN');
  const handleShowAllPlayers = async (e) => {
    console.log(csrfToken);
    const res = await fetch('https://www.fantasyfootballnerd.com/service/players/json/zj6uirc6rfwr/');
    const data = await res.json();
    console.log(data);
    players.length ? console.log(true) : console.log(false)
  }

  return (
    <>
      <Typography variant='h1'>This is the Available Players page</Typography>
      <Button onClick={handleShowAllPlayers}>Show Available Players</Button>
      {players.length ?
        <div>

        </div>
      : null}
    </>
  )
}

export default AvailPlayers;
