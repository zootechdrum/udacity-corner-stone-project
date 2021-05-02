import logo from './logo.svg';
import './App.css';

import {
  BrowserRouter as Router,
  Route,
  Switch
} from 'react-router-dom'

import Grid from '@material-ui/core/Grid';
import AddActorForm from './components/Form/actorForm'
import AddMovieForm from './components/Form/movieForm'
import Main from './pages/main'
import NavBar from './components/Navbar/navbar'
import { Fragment } from 'react';

function App() {
  return (
<>
  <NavBar/>
      <Router>
        <Switch>
          <Route exact path="/" component={Main} />
          <Route exact path="/addactor" component={AddActorForm} />
          <Route exact path="/addmovie" component={AddMovieForm} />
        </Switch>
      </Router>
</>
  )
}

export default App;
