import React, { useEffect, useState }from 'react';
import { BrowserRouter, Switch, Route, NavLink } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import LoginPage from './pages/LoginPage';
import SignupPage from './pages/SignupPage';
import MyTeamPage from './pages/MyTeamPage';
import AvailPlayers from './pages/AvailPlayers';
import SplashPage from './pages/SplashPage';
import { setUser } from './store/auth'
import UserList from './components/UsersList';


function App() {
    // const [loading, setLoading] = useState(true)
    // const dispatch = useDispatch()
    // useEffect(() => {
    //     const loadUser = async () => {
    //         const res = await fetch("/api/users/current_user");
    //         if (res.ok) {
    //             res.data = await res.json(); // current user info
    //             dispatch(setUser(res.data.user))
    //         }
    //         setLoading(false);
    //     }
    //     loadUser();
    // }, [dispatch]);
    const user = localStorage.getItem('user');
    const currentUser = useSelector(state => state.auth);
    console.log(currentUser);
    console.log("____Rendering app_____")
    // if (loading) {
    //     return <p>loading...</p>
    //   }
    return (
        <BrowserRouter>
            <Switch>
                <Route exact path="/users" component={UserList}></Route>
                <Route exact path='/login' component={LoginPage}></Route>
                <Route exact path='/signup' component={SignupPage}></Route>
                { user &&
                    <Route exact path='/myTeam/:id' component={MyTeamPage}></Route>
                }
                { user &&
                    <Route exact path='/players' component={AvailPlayers}></Route>
                }
                <Route path="/" component={SplashPage}></Route>
            </Switch>
        </BrowserRouter>
    );
}

export default App;
