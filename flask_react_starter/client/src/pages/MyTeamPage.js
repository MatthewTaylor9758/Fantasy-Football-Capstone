import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { NavLink } from 'react-router-dom';
import { makeStyles, Container, TextField, Button, Typography } from '@material-ui/core';

function MyTeamPage() {
  const dispatch = useDispatch();

  return (
    <>
      <Typography variant='h1'>This is the My Team Page</Typography>
    </>
  )
}

export default MyTeamPage;
