import React from 'react';

function rand() {
    return Math.round(Math.random() * 20) - 10;
  }
  
  function getModalStyle() {
    const top = 50 + rand();
    const left = 50 + rand();
  
    return {
      top: `${top}%`,
      left: `${left}%`,
      transform: `translate(-${top}%, -${left}%)`,
    };
  }

export default function ActorModal({center, paper}) {
    const [modalStyle] = React.useState(getModalStyle);
    return (
        <div style={center}  className={paper}>
            <h1>This is a modal</h1>
        </div>

    )
}