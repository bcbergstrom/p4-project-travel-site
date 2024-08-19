import React from "react";
import { useState } from "react";
import MenuDropdown from "./Dropdown";

 export default function Allquestions(){
    // cosnt [cboxes, setcboxes] = useState(false)
    const [allquest, setallquest]= useState([])
    // function howPacked(){
    //     let h
    // }
        // <script>
        // function checkNo(){
        //     const checkbox = document.getElementById('styleS');
        //     const text = document.getElementById('text');
        //     if (checkbox.checked == true){
        //         text.style.display = "block";
        //     } else {
        //         text.style.display = "none";
        //     }
        // }
        // </script>
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
         {/* <input type="checkbox" id="styleS" onclick="myFunction()"/> */}
            {/* <p id="text" style="display:none">Checkbox is CHECKED!</p> */}
            <label for="styleS">Shirts</label>
            <input type="checkbox" id="styleS" name="StyleShirts" onclick="myFunction()" />
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
            <MenuDropdown/>
            </div>
            
        {/* </form> */}
        </>
    )
}
