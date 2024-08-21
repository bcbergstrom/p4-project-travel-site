import { useState } from 'react'
import './css/bootstrap.scss'
import Allquestions from './components/Questions'
import ShowLuggage from './components/Luggage'
import Login from './components/Login'
import Register from './components/Register'
import {
  RouterProvider,
  Route,
  Link,
  createBrowserRouter
} from 'react-router-dom'


function App() {
  const router = createBrowserRouter([
    {
      path: "/",
      element: <Login/>
    },
    {
      path: "/register",
      element: <Register/>
    },
    {
      path: "/questions",
      element: <Allquestions/>
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
