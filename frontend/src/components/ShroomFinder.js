import React, { useState } from 'react';

// import axios from 'axios'
// import fileDownload from 'js-file-download'
import { Button, Image } from 'react-bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

//import { Link } from 'react-router-dom'

// Componenets
// import Navigation from './Navigation'


const ShroomFinder = () => {

    const [inputFile, setInputFile] = useState({
        file: "",
    })

    const handleSubmit = () => {
        const formData = new FormData();

        formData.append('File', inputFile);

        console.log(inputFile);

        fetch(
            'http://localhost:3001/evaluate',
            {
                method: 'POST',
                body:  formData,
                mode: 'no-cors',
                // headers: {
                //      'Content-Type': 'application/json'
                //     //'Content-Type': 'multipart/form-data'
                //   },
            }
        ).then((response) => response.json())
            .then((result) => {
                console.log('Success:', result);
            })
            .catch((error) => {
                console.error('Error:', error);
            });
    }

    const onChange = e => {
        e.preventDefault()
        // console.log(e.target.files[0])
        setInputFile({
            ...inputFile,
            [e.target.name]: e.target.files[0],
        })
        console.log(inputFile.file)
    }

    return (
        <div className="d-flex justify-content-center">
            <h1>ShroomFinder</h1>
            <Image src={inputFile.file} alt="pic" style={{ height: "45%", width: "45%" }} thumbnail />
            <input type="file" onChange={onChange} accept="image/png, image/jpeg" name="file" />
            <Button variant="outline-dark"  onClick={handleSubmit}>Evaluate</Button>
        </div>
    );

}

export default ShroomFinder;