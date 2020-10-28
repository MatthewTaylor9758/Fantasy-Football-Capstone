import React, { useEffect, useState } from 'react';
import { login } from '../store/auth'
import { useDispatch, useSelector } from 'react-redux';
import { NavLink } from 'react-router-dom';
import { makeStyles, Container, TextField, Button, Card, Typography } from '@material-ui/core';
import NavBar from '../components/NavBar';
import { getTeam } from '../store/teams';
import '../styles/loginPage.css';
import hiclipart_football from '../images/hiclipart_football.png';

function LoginPage() {
  const dispatch = useDispatch();
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [errors, setErrors] = useState([])
  // let errors = ['testError'];
  // const [userInfo, setUserInfo] = useState(useSelector(state => state.auth));

  const handleUsername = (e) => {
    setUsername(e.target.value);
  }

  const handlePassword= (e) => {
    setPassword(e.target.value);
  }

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!username || !password) {
      setErrors('Please enter a username and password')
    } else {
      const res = await dispatch(login(username, password))
      // console.log(await res.json());
      // ***TO DO***: Set up a second (or more) conditional dispatch(s) for grabbing a team, league, and ffsplayers for that team/league USE 'res' TO DO IT!!!
      console.log(res);
      if (res['1']) {
        console.log(res['1'])
        setErrors(Object.values(res['1']));
      } else {
        debugger
        await dispatch(getTeam(res.user.id))
        window.location.href = `./myTeam/${res.user.id}`
      }
    }
    // setUserInfo()
    // handleInfoGathering()
  }

  // const handleInfoGathering = async (e) => {
  //   console.log(userInfo);
  // }

  const useStyles = makeStyles((theme) => ({
    loginForm: () => {
      return {
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        height: 'fit-content',
        width: '100%',
        padding: '2em 0',
        backgroundColor: 'rgba(255, 255, 255, .15)',
        backdropFilter: '5px',
        borderRadius: '10px'
      }
    },
    outerContainer: {
      width: '100vw',
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
      height: '100vh',
    },
    links: {
      textDecoration: 'none',
      fontFamily: '"Roboto", "Helvetica", "Arial", sans-serif',
      padding: '.7em',
      zIndex: '10',
      '&:hover': {
        color: 'white'
      }
    },
    header: {
      fontFamily: 'Rockwell'
    },
    errorItem: {
      listStyleType: 'none',
      color: 'rgb(200, 0, 0)',
      fontWeight: '400',
      padding: '.3em'
    },
    spacing: {
      padding: '.3em 0'
    },
    loginButton: {
      padding: '.3em',
      marginTop: '.3em',
      '&:hover': {
        backgroundColor: 'blue',
        color: 'white'
      }
    },
    signupButton: {
      backgroundColor: 'rgba(255, 255, 255, .15)',
      marginTop: '1em',
      borderRadius: '10px',
      padding: '0',
      '&:hover': {
        backgroundColor: 'rgba(110, 12, 25, 1)',
      }
    },
    homeButton: {
      backgroundColor: 'rgba(255, 255, 255, .15)',
      marginTop: '1em',
      borderRadius: '10px',
      padding: '0',
    }
  }));

  const classes = useStyles();

  return (
    <>
      <div class='area'>
        <Card id='login-form' className={classes.outerContainer}>
          <ul class="footballs">
              <div><img src={hiclipart_football}></img></div>
              <div><img src={hiclipart_football}></img></div>
              <div><img src={hiclipart_football}></img></div>
              <div><img src={hiclipart_football}></img></div>
          </ul>
          <div>
            <form method='put' action='/api/users/' onSubmit={handleSubmit} className={classes.loginForm}>
              <Typography variant='h4' className={classes.header}>FFStockpile</Typography>
              {errors ? <div className={classes.errorItem}>{errors}</div> : null}
              <TextField
                id='standard-basic'
                className={classes.spacing}
                type='text'
                label='Username'
                value={username}
                onChange={handleUsername}/>
              <TextField
                id='standard-basic'
                className={classes.spacing}
                type='password'
                label='Password'
                value={password}
                onChange={handlePassword}/>
              <Button className={classes.loginButton} type='submit'>Log in</Button>
            </form>
            <div style={{display: 'flex', flexDirection: 'column'}}>
              <Button className={classes.signupButton}>
                <NavLink to='/signup' className={classes.links}>Don't have an account? Sign up</NavLink>
              </Button>
              <Button className={classes.homeButton}>
                <NavLink to='/' className={classes.links}>Home</NavLink>
              </Button>
            </div>
          </div>
        </Card>
      </div>
    </>
  )
}

export default LoginPage;
