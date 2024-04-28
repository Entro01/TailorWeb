import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import './fabric.css';

const Fabric = () => {
    const [fabrics, setFabrics] = useState([]);

    useEffect(() => {
        // Fetch the list of fabrics from the API
        fetch('/fabrics')
            .then(response => response.json())
            .then(data => {
                setFabrics(data.fabrics);
            })
            .catch(error => console.error('Error fetching fabrics:', error));
    }, []);

    return (
        <div className="fabric-home-page">
            <h1>Select a Fabric</h1>
            <div className="fabric-cards-container">
                {fabrics.map((fabric, index) => (
                    <div key={index} className="fabric-card">
                        <img src={fabric.image} alt={fabric.name} className="fabric-image" />
                        <div className="fabric-info">
                            <h3>{fabric.name}</h3>
                            <p>{fabric.description}</p>
                            <Link to={`/product/${encodeURIComponent(fabric.productName)}`} className="fabric-link">
                                View Product
                            </Link>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default Fabric;
