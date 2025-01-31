import React, { useState, useEffect } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { motion } from "framer-motion";

export default function CircularEconomyPlatform() {
  const [materials, setMaterials] = useState([]);
  const [query, setQuery] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchMaterials();
  }, []);

  const fetchMaterials = async (searchQuery = "") => {
    setLoading(true);
    try {
      const res = await fetch(`/api/materials?query=${searchQuery}`);
      if (!res.ok) throw new Error("Failed to fetch materials");
      const data = await res.json();
      setMaterials(data);
      setError(null);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleSearch = () => {
    fetchMaterials(query);
  };

  return (
    <div className="p-6">
      <h1 className="text-xl font-bold mb-4">AI-Powered Circular Economy Platform</h1>
      <div className="flex gap-2 mb-4">
        <Input value={query} onChange={(e) => setQuery(e.target.value)} placeholder="Search materials..." />
        <Button onClick={handleSearch}>Search</Button>
      </div>
      {loading && <p>Loading materials...</p>}
      {error && <p className="text-red-500">Error: {error}</p>}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {materials.length > 0 ? (
          materials.map((material, index) => (
            <motion.div key={index} whileHover={{ scale: 1.05 }}>
              <Card className="p-4">
                <CardContent>
                  <h2 className="text-lg font-semibold">{material.name}</h2>
                  <p>{material.description}</p>
                  <Button className="mt-2">View Details</Button>
                </CardContent>
              </Card>
            </motion.div>
          ))
        ) : (
          !loading && <p>No materials found.</p>
        )}
      </div>
    </div>
  );
}
