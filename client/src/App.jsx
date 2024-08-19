import { useState } from 'react'
import 'bootstrap/scss/bootstrap.scss'
import Allquestions from './components/Questions'


function App() {
  const [count, setCount] = useState(0)

  return (
    <div>
     <Allquestions/>
    </div>
  )
}

export default App
