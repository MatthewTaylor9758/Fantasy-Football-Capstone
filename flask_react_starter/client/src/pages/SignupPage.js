import React, { useEffect, useState } from 'react';
import { signup } from '../store/auth';
import { useDispatch, useSelector } from 'react-redux';
import { NavLink } from 'react-router-dom';
import { makeStyles, Container, TextField, Button } from '@material-ui/core';

function SignupPage() {
  const dispatch = useDispatch();
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [errors, setErrors] = useState([]);

  const handleUsername = (e) => {
    setUsername(e.target.value);
  };

  const handleEmail = (e) => {
    setEmail(e.target.value);
  };

  const handlePassword = (e) => {
    setPassword(e.target.value);
  };

  const handleConfirmPassword = (e) => {
    setConfirmPassword(e.target.value);
  };

  useEffect(() => {
    console.log(Object.values(errors))
  }, [errors])

  const handleSubmit = async (e) => {
    e.preventDefault()
    if (!username || !email || !password || !confirmPassword) {
      await setErrors(['Please fill out all fields.'])
      console.log(errors)
    } else {
      const res = await dispatch(signup(username, email, password))
      console.log(res);
      setErrors(Object.values(res))
      console.log(errors);
    }
  }

  return (
    <>
      {errors ? <ul>
                  {errors.map((error, index) => <li key={index}>{error}</li>)}
                </ul> : null}
      <form action='/api/users/' method='post' onSubmit={handleSubmit}>
        <TextField type='text' placeholder='Username' value={username} onChange={handleUsername}/>
        <TextField type='email' placeholder='Email' value={email} onChange={handleEmail}/>
        <TextField type='password' placeholder='Password' value={password} onChange={handlePassword}/>
        <TextField type='password' placeholder='Confirm Password' value={confirmPassword} onChange={handleConfirmPassword}/>
        <Button type='submit'>Sign up</Button>
      </form>
    </>
  )
}

export default SignupPage;
