const Actor = {
    delete: function(id, token) {
        fetch('/actors/' + id, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
                Authorization: `Bearer ${token}`
            },

        })
    }
}

export default Actor