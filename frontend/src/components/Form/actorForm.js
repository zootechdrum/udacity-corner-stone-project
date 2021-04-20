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

  const onChangeForGender = (event) => {
    setGender(event.target.value)
  }

  const onChangeForAge = (event) => {
    setAge(event.target.value)
  }

  const onChangeForName= (event) => {
    setName(event.target.value)
  }

    const submit = () => {
      const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name: name, age: age, gender: gender })
    };

      fetch('/add_actor', requestOptions) 
      .then(res => console.log(res.json()))
  }


  

  return (
    <Grid item style={{ backgroundColor: 'yellow' }}>
      <h2>Add an Actor</h2>
      <form noValidate autoComplete="off">
        <Input placeholder="Actors Full Name" onChange={onChangeForName} inputProps={{ 'aria-label': 'description' }} />
        <Input placeholder="Gender" onChange={onChangeForGender} inputProps={{ 'aria-label': 'description' }} />
        <Input placeholder="age" onChange={onChangeForAge}  inputProps={{ 'aria-label': 'description' }} />
      </form>
      <Button variant="contained" onClick={submit} color="secondary">
        Add an Actor
</Button>
    </Grid>
  )

}

export default AddActorForm;