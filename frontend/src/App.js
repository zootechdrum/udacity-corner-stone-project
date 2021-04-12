import logo from './logo.svg';
import './App.css';

import Grid from '@material-ui/core/Grid';
import AddActorForm from './components/FormView'

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
    <AddActorForm />
  </Grid>
);
}

export default App;
