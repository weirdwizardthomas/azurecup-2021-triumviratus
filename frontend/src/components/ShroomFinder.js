import React, { useState } from 'react';

// import axios from 'axios'
// import fileDownload from 'js-file-download'
import { Button, Image } from 'react-bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

//import { Link } from 'react-router-dom'

// Componenets
// import Navigation from './Navigation'


const ShroomFinder = () => {
    var imgsrc = ""

    const [inputFile, setInputFile] = useState({
        file: "",
    })

    const [tablerows, setTableRows] = useState([])

    const handleSubmit = () => {
        const formData = new FormData();

        formData.append('File', inputFile.file);

        console.log(inputFile.file);

        fetch(
            'http://localhost:3001/evaluate',
            {
                method: 'POST',
                body: formData,// JSON.stringify(jobject),
                //mode: 'cors',
                // headers: {
                //     //'Accept': 'application/json',
                //     //'Content-Type': 'application/json'
                //     'Content-Type': 'multipart/form-data'
                //   },
            }
        ).then((response) => response.json())
            .then((result) => {
                console.log('Success:', result.name);
                setTableRows(result.predictions)
                document.getElementById("rows").innerHTML = JSON.stringify(result.predictions)
                //getRowsData()
            })
            .catch((error) => {
                console.error('Error:', error);
            });
    }

    const onChange = e => {
        e.preventDefault()
        // console.log(e.target.files[0])
        var image = document.getElementById('pic');
        image.src = URL.createObjectURL(e.target.files[0]);

        setInputFile({
            ...inputFile,
            [e.target.name]: e.target.files[0],
        })
        console.log(inputFile.file)
    }

    return (
        <div className="d-flex flex-column align-items-center block">
            <h1 style={{color: "white"}}>ShroomFinder</h1>
            <Image src={imgsrc} alt="pic" style={{ height: "45%", width: "45%" }} id="pic" thumbnail />
            <input type="file" onChange={onChange} accept="image/png, image/jpeg" name="file" />
            <Button variant="outline-light" size="lg" onClick={handleSubmit}>Evaluate</Button>
            <div id="rows" style={{color: "white"}}></div>
        </div>
    );

}

export default ShroomFinder;