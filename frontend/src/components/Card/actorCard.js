import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';

const useStyles = makeStyles({
  root: {
    minWidth: 275,
    marginTop:'5px'
  },
  bullet: {
    display: 'inline-block',
    margin: '0 2px',
    transform: 'scale(0.8)',
  },
  title: {
    fontSize: 14,
  },
  pos: {
    marginBottom: 12,
  },
});

export default function ActorCard({actorName, deleteBtn, id, dltMve,updtBtn, openMdl}) {
  const classes = useStyles();



  return (
    <Card key={id}  className={classes.root}>
      <CardContent>
        <Typography className={classes.title} color="textSecondary" gutterBottom>
         {actorName}
        </Typography>
        <Typography className={classes.pos} color="textSecondary">
          {deleteBtn && <Button id={id} onClick={dltMve} variant="contained" color="secondary">Delete an Actor</Button>}
        </Typography>
        <Typography variant="body2" component="p">
          {updtBtn && <Button id={id} onClick={openMdl}  variant="contained" color="primary">Update an Actor</Button>}
          <br />
          {'"a benevolent smile"'}
        </Typography>
      </CardContent>
      <CardActions>
        <Button size="small">Learn More</Button>
      </CardActions>
    </Card>
  );
}