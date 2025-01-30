CREATE INDEX idx_weather_date ON weather_data (date);
CREATE INDEX idx_crop_yield_date ON crop_yield_data (date);
CREATE INDEX idx_crop_yield_region ON crop_yield_data (region);
CREATE INDEX idx_weather_region ON weather_data (region);