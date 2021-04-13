import React from 'react'
import Grid from '@material-ui/core/Grid';
import { makeStyles } from '@material-ui/core/styles';
import Input from '@material-ui/core/Input';


const AddActorForm = () => {
 return (
    <Grid item style={{ backgroundColor: 'yellow' }}>
      <h2>Add an Actor</h2>
    <form  noValidate autoComplete="off">
      <Input placeholder="Actors Full Name" inputProps={{ 'aria-label': 'description' }} />
      <Input placeholder="Gender" inputProps={{ 'aria-label': 'description' }} />
      <Input placeholder="age" inputProps={{ 'aria-label': 'description' }} />
      </form>
    </Grid>
 )

}

export default AddActorForm;