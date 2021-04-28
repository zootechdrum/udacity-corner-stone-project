import React from "react";
import { useAuth0} from "@auth0/auth0-react";
import { Auth0Client, Auth0ClientOptions } from "@auth0/auth0-spa-js";

const Main = () => {
    const { isAuthenticated } = useAuth0();
    const {getAccessTokenSilently} = useAuth0(); 
    
    const data = async() => {
        if (isAuthenticated) {

            try {

                const token = await getAccessTokenSilently();
                console.log(token)
                const resonse = await fetch('/actors', {
                    headers: {
                        Authorization: `Bearer ${token}`
                    }
                })
                console.log(resonse)
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