import React, { useEffect, useState } from 'react';
import { signup, login } from '../store/auth';
import { useDispatch, useSelector } from 'react-redux';
import { NavLink } from 'react-router-dom';
import { makeStyles, Container, TextField, Button, Card, Typography } from '@material-ui/core';
import NavBar from '../components/NavBar';
import { red } from '@material-ui/core/colors';
import '../styles/signupPage.css';

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
    setErrors([])
    if (!username || !email || !password || !confirmPassword) {
      await setErrors(['Please fill out all fields.'])
      console.log(errors)
    } else {
      if (password === confirmPassword) {
        const res = await dispatch(signup(username, email, password))
        console.log(res)
        if (res.errors) {
          console.log(res);
          debugger
          setErrors(Object.values(res.errors))
          console.log(errors);
        } else {
          await dispatch(login(username, password));
          window.location.href = `./myTeam/${res.user.id}`;
        }
      }
    }
  }

  const useStyles = makeStyles((theme) => ({
    signupForm: () => {
      return {
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        height: 'fit-content',
        width: 'fit-content',
        padding: '2em',
        backgroundColor: 'rgba(255, 255, 255, .15)',
        backdropFilter: '5px',
        borderRadius: '10px',
        padding: '2em 3em'
      }
    },
    outerContainer: {
      width: '100vw',
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
      height: '100vh',
      background: 'linear-gradient(-45deg, rgba(255, 255, 255, .2),  rgba(25, 111, 12, .7))',
    },
    links: {
      textDecoration: 'none',
      fontFamily: '"Roboto", "Helvetica", "Arial", sans-serif'
    },
    header: {
      fontFamily: 'Rockwell'
    },
    spacing: {
      marginTop: '.3em'
    },
    errorList: {
      padding: '0',
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
    },
    errorUL: {
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      margin: '.3em 0 0 0',
      padding: '0'
    },
    errorItem: {
      listStyleType: 'none',
      color: 'rgb(200, 0, 0)',
      fontWeight: '400'
    },
    passwordConfirm: () => {
      return {
        marginTop: '.3em',
        borderRadius: '3px',
        backgroundColor: confirmPassword !== password ? 'rgba(255, 0, 0, .3)' : 'rgba(255, 255, 255, 0)',
      }
    },
    signupButton: {
      marginTop: '1em',
      '&:hover': {
        backgroundColor: 'rgba(110, 12, 25, 1)',
        color: 'white'
      }
    }
  }));

  const classes = useStyles();

  return (
    <>

      <div class='area'>
        <Card className={classes.outerContainer}>
            <ul class="footballs">
              <li></li>
              <li></li>
              <li></li>
              <li></li>
            </ul>

          <form action='/api/users/' method='post' onSubmit={handleSubmit} className={classes.signupForm}>
            <Typography variant='h4' className={classes.header}>FFStockpile</Typography>
            {errors ? <div className={classes.errorList}>
                        <ul className={classes.errorUL}>
                          {errors.map((error, index) => <li key={index} className={classes.errorItem}>{error}</li>)}
                        </ul>
                      </div>
            : null}
            {/* <TextField id="standard-basic" label="Standard" /> */}
            <TextField
              id='standard-basic'
              className={classes.spacing}
              type='text'
              value={username}
              onChange={handleUsername}
              label='Username'
              />
            <TextField
              id='standard-basic'
              className={classes.spacing}
              type='email'
              label='Email'
              value={email}
              onChange={handleEmail} />
            <TextField
              id='standard-basic'
              className={classes.spacing}
              type='password'
              label='Password'
              value={password}
              onChange={handlePassword} />
            <TextField
              id='standard-basic'
              className={classes.spacing}
              type='password'
              label='Confirm Password'
              value={confirmPassword}
              onChange={handleConfirmPassword}
              inputProps={{
                className: classes.passwordConfirm
              }}
              />
            <Button type='submit' className={classes.signupButton}>Sign up</Button>
          </form>
        </Card>
      </div>
    </>
  )
}

export default SignupPage;
