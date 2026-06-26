export default async function handler(req, res) {
  const CLIENT_ID = "1455ea4d286148fb8026b4f162c008c3";
  const CLIENT_SECRET = "0EaEC1da661F4Bf6B3B847272499Dac3";
  const url = `https://apitransporte.buenosaires.gob.ar/subtes/serviceAlerts?client_id=${CLIENT_ID}&client_secret=${CLIENT_SECRET}&json=1`;
  try {
    const data = await fetch(url).then(r => r.json());
    res.setHeader('Content-Type', 'application/json');
    res.json(data);
  } catch(e) {
    res.status(500).json({ error: e.message });
  }
}
