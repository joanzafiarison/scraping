import React, {useState} from 'react'

function ScreenPanel({result}) {
    const [dataKeys, setDataKeys] = useState({});
    const [modifiedHtml, setModifiedHtml] = useState(result.html)
  return (
    <div>
        <h2>SnapShot Verification</h2>
        <div>
            {modifiedHtml}
        </div>
        
        <table>
            <thead>
                <tr>
                    <th>Attribut</th>
                </tr>
                <tr>
                    <th>Valeur</th>
                </tr>
                <tr>
                    <th>Selecteur</th>
                </tr>
            </thead>
            <tbody>
                {result.data.map( (el, k) => (
                    <tr key={k}>
                        <td>{el.attr}</td>
                        <td>{el.value}</td>
                        <td>{el.selector}</td>
                    </tr>
                ))}
            </tbody>
        </table>
    </div>
  )
}

export default ScreenPanel