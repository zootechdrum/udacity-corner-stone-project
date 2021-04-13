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

function App() {
  return (
    <Grid
    container
    spacing={0}
    align="center"
    justify="center"
    direction="column"
    style={{ backgroundColor: 'teal' }}
  >
      <Router>
        <Switch>
          <Route path="/addactor" component={AddActorForm} />
          <Route path="/addmovie" component={AddMovieForm} />
        </Switch>
      </Router>
      </Grid>
  )


}

export default App;
