import { useState } from 'react'
import 'bootstrap/scss/bootstrap.scss'
import Allquestions from './components/Questions'
import MenuDropdown from './components/Dropdown'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div>
      <MenuDropdown/>
     <Allquestions/>
    </div>
  )
}

export default App
