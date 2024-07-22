import React, { useState } from 'react';
import axios from 'axios';
import Papa from 'papaparse';
const DataForm = () => {
    const [sensorId, setSensorId] = useState('');
    const [location, setLocation] = useState('');
    const [startTime, setStartTime] = useState('');
    const [endTime, setEndTime] = useState('');
    const [data, setData] = useState(null);

    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
            const response = await axios.get('${process.env.REACT_APP_API_URL_GET}', {
                params: {
                    sensor_id: sensorId || undefined,
                    location: location || undefined,
                    start_time: startTime ? new Date(startTime).toISOString() : undefined,
                    end_time: endTime ? new Date(endTime).toISOString() : undefined,
                },
            });
            setData(response.data);
        } catch (error) {
            console.error("Error while fetching the data: ", error);
        }
    };

    const handleDownloadCSV = () => {
        const csv = Papa.unparse(data);

        const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
        const url = URL.createObjectURL(blob);
        const link = document.createElement('a');
        link.setAttribute('href', url);
        link.setAttribute('download', 'sensor_data.csv');
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Sensor ID:</label>
                    <input type="text" value={sensorId} onChange={(e) => setSensorId(e.target.value)} />
                </div>
                <div>
                    <label>Location:</label>
                    <input type="text" value={location} onChange={(e) => setLocation(e.target.value)} />
                </div>
                <div>
                    <label>Start Time:</label>
                    <input type="datetime-local" value={startTime} onChange={(e) => setStartTime(e.target.value)} />
                </div>
                <div>
                    <label>End Time:</label>
                    <input type="datetime-local" value={endTime} onChange={(e) => setEndTime(e.target.value)} />
                </div>
                <button type="submit">Fetch Data</button>
            </form>
            {data && data.length > 0 && (
                <div>
                    <h3>Data:</h3>
                    <button onClick={handleDownloadCSV}>Download CSV</button>
                    <table>
                        <thead>
                            <tr>
                                <th>ID</th>
                                <th>Sensor ID</th>
                                <th>Location</th>
                                <th>Value</th>
                                <th>Timestamp</th>
                            </tr>
                        </thead>
                        <tbody>
                            {data.map((item) => (
                                <tr key={item.id}>
                                    <td>{item.id}</td>
                                    <td>{item.sensor_id}</td>
                                    <td>{item.location}</td>
                                    <td>{item.value}</td>
                                    <td>{new Date(item.time_stamp).toLocaleString()}</td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            )}
        </div>
    );
};

export default DataForm;