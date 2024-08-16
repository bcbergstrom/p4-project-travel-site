import React from "react";
import { useState } from "react";
import MenuDropdown from "./Dropdown";

 export default function Allquestions(){
    // cosnt [cboxes, setcboxes] = useState(false)
    const [allquest, setallquest]= useState([])
    return(
        <>
        <h1>Lets get started by packing your luggage!</h1>
        {/* <form onSubmit={(e)=>
            e.preventDefault()
            const pLuggage = {
                styleS = e.target['StyleShirts'].value, 
                styleP = e.target['StylePants'].value, 
                styleA = e.target['StyleAccessories'].value, 
                iSum = e.target['IsSummer'].value, 
                aP = e.target['Pants'].value, 
                aS = e.target['Shirts'].value, 
                aO = e.target['OtherClothes'].value, 
                wS = e.target['WorryScale'].value 
            }

        }> */}
         <div>
            <label for="styleS">Shirts</label>
            <input type="checkbox" id="styleS" name="scales" check />
            <input type="checkbox" id="styleS" name="StyleShirts" check />
            <label for="styleP">Pants</label>
            <input type="checkbox" id="styleP" name="StylePants" check />
            <input type="checkbox" id="styleP" name="StylePants" check />
            <label for="styleA">Accessories</label>
            <input type="checkbox" id="styleA" name="StyleAccessories" check />
            <input type="checkbox" id="styleA" name="StyleAccessories" check />
            <label for="styleA">Summer</label>
            <input type="checkbox" id="iSum" name="IsSummer" check />
            <input type="checkbox" id="iSum" name="IsSummer" check />
            </div>
            
        {/* </form> */}
        </>
    )
}
{/* <div class="dropdown">
    <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">dropsown</button>
    <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
        <a class="dropdown-item" href="#">Action</a>
        <a class="dropdown-item" href="#">Another action</a>
        <a class="dropdown-item" href="#">Something else here</a>
        </div>
        </div> */}