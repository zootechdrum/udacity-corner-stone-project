import React from "react";
import { useAuth0} from "@auth0/auth0-react";
import jwt_decode from "jwt-decode";

const Main = () => {
    const { isAuthenticated } = useAuth0();
    const {getAccessTokenSilently} = useAuth0(); 
    
    const data = async() => {
        if (isAuthenticated) {

            try {

                const token = await getAccessTokenSilently();
                const decoded = jwt_decode(token)
                console.log(decoded)
                let response = await fetch('/actors', {
                    headers: {
                        Authorization: `Bearer ${token}`
                    }
                })
                const data = await response.json()
                console.log(data)
            }
            finally{
                console.log("Nothing")
            }

    }
}

data()

  return (
      <div>
          <h1>Hje</h1>
      </div>

  )};

export default Main;