# DESIGN.md

## System Architecture

The AI Store Intelligence System processes CCTV footage and generates visitor analytics through a modular pipeline.

### Detection Layer

YOLOv8 is used to detect people from CCTV frames.

### Tracking Layer

ByteTrack assigns unique IDs to detected visitors and maintains tracking consistency across frames.

### Entry Analytics

Visitor IDs crossing the entry region are counted as store entries.

### Event Generation

Each visitor action is converted into structured event records.

### Analytics Layer

Aggregated visitor statistics are exposed through FastAPI endpoints.

### API Layer

FastAPI provides REST APIs for health monitoring and visitor analytics.

## Production Considerations

* Modular pipeline architecture
* Event-driven analytics
* Lightweight deployment
* Extensible API layer

## AI-Assisted Decisions

AI tools were used for:

* Architecture brainstorming
* Documentation drafting
* API design guidance
* Development workflow support

All implementation, testing, debugging, and integration decisions were performed manually.
