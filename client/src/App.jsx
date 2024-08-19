import { useState } from 'react'
import './css/bootstrap.scss'
import Allquestions from './components/Questions'
import ShowLuggage from './components/Luggage'


function App() {
  const [count, setCount] = useState(0)

  return (
    <div>
      {/* <ShowLuggage/> */}
     <Allquestions/>
    </div>
  )
}

export default App
