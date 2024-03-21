-- List all bands with Glam rock as their main style, ranked longevity

SELECT band_name,
    CASE
        WHEN split IS NOT NULL THEN 2022 - CAST(split AS UNSIGNED)
        ELSE 2022 - CAST(formed AS UNSIGNED)
    END AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC, band_name;
