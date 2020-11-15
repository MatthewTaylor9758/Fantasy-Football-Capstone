import React, { useEffect, useState } from 'react';
import { NavLink } from 'react-router-dom';
import { useSelector } from 'react-redux';
import { makeStyles, Container, TextField, Button, Typography, Grid } from '@material-ui/core';
import NavBar from '../components/NavBar';
import stats_picture from '../images/stats_picture.png';
import data_image from '../images/data_image.jpg';
import players_background from '../images/players_background.jpg';
import Footer from '../components/Footer';

function SplashPage() {
  const user = useSelector(state => state.auth)

  const useStyles = makeStyles({
    background: {
      // backgroundImage: 'linear-gradient(-45deg, rgba(255, 255, 255, .2), rgba(25, 111, 12, .7))',
      width: '100%'
    },
    outerContainerUpper: {
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
      // backgroundImage: 'linear-gradient(-135deg, rgba(255, 255, 255, .2), rgba(25, 111, 12, .7))',
      width: '100%',
      padding: '3% 0 3% 0',
    },
    outerContainerLower: {
      // backgroundImage: 'linear-gradient(-45deg, rgba(255, 255, 255, .2), rgba(25, 111, 12, .7))',
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
      width: '100%',
      padding: '0 0 3% 0',
    },
    footer: {
      // backgroundImage: 'linear-gradient(-45deg, rgba(255, 255, 255, .2), rgba(25, 111, 12, .7))',
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
      width: '100%',
      padding: '0 0 3% 0'
    },
    upperImage: {
      width: '90%',
      maxWidth: '90%',
      maxHeight: '90%',
      // opacity: '.3'
      borderRadius: '4px'
    },
    footerImage: {
      width: '100%',
      height: '60%'
    },
    textContainer: {
      display: 'flex',
      justifyContent: 'center',
      position: 'absolute',
      top: '20%'
    },
    imageContainerTop: {
      display: 'flex',
      justifyContent: 'flex-end',
      alignItems: 'center',
      borderTop: '1px solid black'
    },
    imageContainerBottom: {
      display: 'flex',
      justifyContent: 'flex-start',
      alignItems: 'center',
      borderTop: '1px solid black'
    },
    // imageText: {
    //   // position: 'absolute',
    //   // top: '40px',
    //   display: 'flex',
    //   flexDirection: 'column',
    //   alignItems: 'center',
    //   zIndex: '1',
    //   width: 'fit-content',
    //   height: 'fit-content',
    //   padding: '10px',
    //   borderRadius: '10px',
    //   backgroundColor: 'rgba(0, 0, 0, .8)'
    // },
    titleText: {
      fontWeight: '600',
      textAlign: 'center',
      width: '100%',
      marginBottom: '.7em',
      // borderBottom: '1px solid darkgray',
      color: 'rgb(245, 245, 245)'
    },
    pText: {
      fontWeight: '600',
      color: 'rgb(245, 245, 245)'
    },
    pTitleText: {
      fontWeight: '700',
      color: 'rgb(245, 245, 245)'
    },
    gridText: {
      display: 'flex',
      flexDirection: 'column',
      justifyContent: 'center',
      borderTop: '1px solid black'
    }
  })
  const classes = useStyles();

  const test = () => {
    console.log(user);
    localStorage.getItem('user') ? console.log(user) : console.log('no user')
  }

  return (
    <>
      <NavBar />
      <div className={classes.background}>
        <Container className={classes.outerContainerUpper}>
          <Grid container xs={10} spacing={2}>
            <Typography variant='h3' className={classes.titleText}>Welcome to FFStockpile!</Typography>
            <Grid item xs={6} className={classes.gridText}>
              <Typography variant='h4' className={classes.pTitleText}>All the stats you need</Typography>
              <p className={classes.pText}>We give you all the stats you need to make informed decisions. With FFStockpile you'll never have to worry about a lack of information.</p>
            </Grid>
            <Grid item xs={6} className={classes.imageContainerTop}>
              <img src={'https://raw.githubusercontent.com/MatthewTaylor9758/Fantasy-Football-Capstone/main/flask_react_starter/client/src/images/stats_picture.png'} className={classes.upperImage}></img>
            </Grid>
          </Grid>
        </Container>
        <Container className={classes.outerContainerLower}>
          <Grid container xs={10} spacing={2} className={classes.gridContainer}>
            <Grid item xs={6} className={classes.imageContainerBottom}>
              <img src={'https://raw.githubusercontent.com/MatthewTaylor9758/Fantasy-Football-Capstone/main/flask_react_starter/client/src/images/data_image.jpg'} className={classes.upperImage}></img>
            </Grid>
            <Grid item xs={6} className={classes.gridText}>
            <Typography variant='h4' className={classes.pTitleText}>Your data all in one place</Typography>
              <p className={classes.pText}>Never again be forced to jump between websites to find the information you need. From basic stats to the most complex, we have them all, and now you do too. </p>
            </Grid>
          </Grid>
        </Container>
      </div>
    </>
  )
}

export default SplashPage;
