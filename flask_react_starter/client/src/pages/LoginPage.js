import React, { useEffect, useState } from 'react';
import { login } from '../store/auth'
import { useDispatch, useSelector } from 'react-redux';
import { NavLink } from 'react-router-dom';
import { makeStyles, Container, TextField, Button } from '@material-ui/core';

function LoginPage() {
  const dispatch = useDispatch();
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [errors, setErrors] = useState([])
  // let errors = ['testError'];

  const handleUsername = (e) => {
    setUsername(e.target.value);
  }

  const handlePassword= (e) => {
    setPassword(e.target.value);
  }

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!username && !password) {
      setErrors('Please enter a username and password')
    } else {
      const res = await dispatch(login(username, password))
      setErrors(Object.values(res));
    }
  }

  return (
    <>
      {errors ? <div>{errors}</div> : null}
      <form method='put' action='/api/users/' onSubmit={handleSubmit}>
        <TextField type='text' placeholder='Username' value={username} onChange={handleUsername}/>
        <TextField type='password' placeholder='Password' value={password} onChange={handlePassword}/>
        <Button type='submit'>Log in</Button>
      </form>
    </>
  )
}

export default LoginPage;
