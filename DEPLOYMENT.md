# Deployment Guide

## Render Deployment

### Prerequisites
- GitHub repository with your code
- Render account

### 1. Backend Deployment (Render)

1. **Push your code to GitHub** including the `render.yaml` file
2. **Go to Render Dashboard** → https://render.com/
3. **Create New Blueprint**:
   - Click "New" → "Blueprint"
   - Connect your GitHub repository
   - Select your repository
   - Render will automatically detect `render.yaml`
4. **Review and Deploy**:
   - Render will create:
     - FastAPI Web Service
     - PostgreSQL Database
     - Redis Instance
   - Environment variables will be set automatically
   - Database migrations will run on first deploy

### 2. Frontend Deployment (Vercel)

1. **Go to Vercel** → https://vercel.com/
2. **Import Project**:
   - Connect your GitHub repository
   - Set root directory to `frontend`
3. **Environment Variables**:
   ```
   NEXT_PUBLIC_API_URL=https://verifly2-backend.onrender.com
   ```
4. **Deploy**

### 3. Update CORS Origins

After deploying frontend, update the backend CORS origins:

1. **In Render Dashboard**:
   - Go to your backend service
   - Environment → Edit
   - Update `BACKEND_CORS_ORIGINS`:
     ```
     https://your-frontend-url.vercel.app,http://localhost:3000
     ```

### 4. Database Migrations

Migrations run automatically on deployment via `deploy.py` script.

To run manually:
```bash
# In Render shell
alembic upgrade head
```

### 5. Monitoring

- **Backend Health**: https://verifly2-backend.onrender.com/health
- **API Docs**: https://verifly2-backend.onrender.com/docs
- **Logs**: Available in Render dashboard

## Environment Variables

### Backend (Render)
- `ENVIRONMENT=production` (auto-set)
- `SECRET_KEY` (auto-generated)
- `DATABASE_URL` (auto-set from PostgreSQL)
- `REDIS_URL` (auto-set from Redis)
- `BACKEND_CORS_ORIGINS` (set your frontend URL)

### Frontend (Vercel)
- `NEXT_PUBLIC_API_URL` (your Render backend URL)

## Troubleshooting

### Common Issues

1. **CORS Errors**:
   - Ensure `BACKEND_CORS_ORIGINS` includes your frontend URL
   - Check that both HTTP and HTTPS are included if needed

2. **Database Connection**:
   - Verify `DATABASE_URL` is set correctly
   - Check Render logs for connection errors

3. **Migration Errors**:
   - Check logs during deployment
   - Manually run migrations if needed

4. **Environment Variables**:
   - Ensure all required variables are set
   - Check for typos in variable names

### Logs Access

**Render**:
- Dashboard → Your Service → Logs

**Vercel**:
- Dashboard → Your Project → Functions → View Logs

## Production Checklist

- [ ] `render.yaml` configured correctly
- [ ] Environment variables set
- [ ] Frontend deployed to Vercel
- [ ] CORS origins updated
- [ ] Database migrations completed
- [ ] Health endpoints responding
- [ ] SSL certificates active
- [ ] Domain configured (optional)

## Scaling

### Backend (Render)
- Upgrade plan for more resources
- Enable autoscaling
- Add multiple regions

### Database
- Upgrade PostgreSQL plan
- Enable connection pooling
- Set up read replicas

### Frontend (Vercel)
- Automatic scaling included
- CDN distribution worldwide
- Edge functions available
