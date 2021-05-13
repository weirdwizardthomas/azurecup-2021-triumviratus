import React, {useState} from 'react';

import axios from 'axios'
import fileDownload from 'js-file-download'
import {Button, Image} from 'react-bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

//import { Link } from 'react-router-dom'

// Componenets
// import Navigation from './Navigation'


const ShroomFinder = () => {

    const [inputFile, setInputFile] = useState({
        file: "",
    })
    // this.handleDownload = (url, filename) => {
    //     axios.get(url, {
    //       responseType: 'blob',
    //     })
    //     .then((res) => {
    //       fileDownload(res.data, filename)
    //     })
    //   }

      const onChange = e => {
        e.preventDefault()
        console.log(e.target.files[0])
        setInputFile({
            ...inputFile,
            [e.target.name]: URL.createObjectURL(e.target.files[0]) ,
        })
        console.log(inputFile.file)
    }

        return (
            <div className="d-flex justify-content-center">
                <h1>ShroomFinder</h1>
                <Image src={inputFile.file} alt="pic"  thumbnail/>
                <input type="file" onChange={onChange} accept="image/png, image/jpeg" name="file" />
                {/* <Button variant="outline-dark"  onClick={() => {
                    this.handleDownload(this.state.file, 'test-download.png')
                }}>Download Image</Button> */}
            </div>
        );

}

export default ShroomFinder;