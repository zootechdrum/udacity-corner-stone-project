import React from 'react'
import Grid from '@material-ui/core/Grid';
import { makeStyles } from '@material-ui/core/styles';
import Input from '@material-ui/core/Input';
import Button from '@material-ui/core/Button';
import { useState } from 'react';

const AddActorForm = () => {

  const [name, setName] = useState('');
  const [age, setAge] = useState('');
  const [gender, setGender] = useState('');

  const onChangeForGender= (event) => {
    setGender(event.target.value)
}

  const submit = () => {




}

 return (
    <Grid item style={{ backgroundColor: 'yellow' }}>
      <h2>Add an Actor</h2>
    <form  noValidate autoComplete="off">
      <Input placeholder="Actors Full Name" inputProps={{ 'aria-label': 'description' }} />
      <Input placeholder="Gender" inputProps={{ 'aria-label': 'description' }} />
      <Input placeholder="age" inputProps={{ 'aria-label': 'description' }} />
      </form>
      <Button variant="contained" onClick={submit} color="secondary">
  Add an Actor
</Button>
    </Grid>
 )

}

export default AddActorForm;