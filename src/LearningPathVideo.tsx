import React from 'react';
import { VideoPlayer } from './VideoPlayer';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Clock, CheckCircle } from 'lucide-react';

interface LearningPathVideoProps {
  video: {
    id: string;
    title: string;
    topic: string;
    duration: string;
    src: string;
    completed?: boolean;
    description?: string;
  };
  className?: string;
}

export const LearningPathVideo: React.FC<LearningPathVideoProps> = ({
  video,
  className = ""
}) => {
  return (
    <Card className={`bg-white/5 border-white/10 ${className}`}>
      <CardHeader>
        <div className="flex items-start justify-between">
          <div>
            <CardTitle className="text-white text-lg">{video.title}</CardTitle>
            <p className="text-gray-400 text-sm mt-1">{video.description}</p>
          </div>
          <div className="flex items-center gap-2">
            <Badge variant="outline" className="text-gray-300 border-gray-600">
              <Clock className="h-3 w-3 mr-1" />
              {video.duration}
            </Badge>
            {video.completed && (
              <Badge className="bg-green-600 text-white">
                <CheckCircle className="h-3 w-3 mr-1" />
                Completed
              </Badge>
            )}
          </div>
        </div>
      </CardHeader>
      <CardContent>
        <VideoPlayer
          videoId={video.id}
          topic={video.topic}
          src={video.src}
          className="mb-4"
        />
        <div className="text-sm text-gray-400">
          <p>Complete this video to update your career readiness score and get personalized job recommendations.</p>
        </div>
      </CardContent>
    </Card>
  );
};