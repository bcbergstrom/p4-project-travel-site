import React, { useEffect, useState } from 'react'
import './css/bootstrap.scss'
import Allquestions from './components/Questions'
import ShowLuggage from './components/Luggage'
import Places from './components/Activities'
import Trip from './components/Trip'
import Login from './components/Login'
import Register from './components/Register'
import {
  RouterProvider,
  Route,
  Link,
  createBrowserRouter,
  redirect
} from 'react-router-dom'

function App() {
  const [password, setPassword] = useState("")
  const [email, setEmail] = useState("")
  const [user, setUser] = useState(null)
  useEffect(() => {
    fetch('/api/session')
    .then(r=>{
      if (r.ok) { return r.json()}
      else {throw new Error}
    })
    .then(data=>{
      setUser(data)
    })
    .catch(data=>{console.log(data)})
      
  }, [])
  



  const router = createBrowserRouter([
    {
      path: "/",
      element: <Login email={email} setEmail={setEmail} 
                password={password} setPassword={setPassword} 
                user={user} setUser={setUser}/>
    },
    {
      path: "/register",
      element: <Register/>,
    },
    {
      path: "/questions",
      element: <Allquestions user={user} />,
      loader: () => {
       return user ? true: redirect("/")
      }
    }
  ])
  return (
    <div>
      {/* <ShowLuggage/>
     <Allquestions/> */}
    <RouterProvider router={router}/>
    </div>
  )
}

export default App
