from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelSmokeTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create(name='Test User', email='test@example.com', team='Marvel')
        self.assertEqual(user.name, 'Test User')
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team', members=['A', 'B'])
        self.assertEqual(team.name, 'Test Team')
    def test_activity_creation(self):
        activity = Activity.objects.create(user='Test User', activity='Running', duration=30)
        self.assertEqual(activity.activity, 'Running')
    def test_leaderboard_creation(self):
        lb = Leaderboard.objects.create(team='Test Team', points=100)
        self.assertEqual(lb.points, 100)
    def test_workout_creation(self):
        workout = Workout.objects.create(user='Test User', workout='Pushups', reps=50)
        self.assertEqual(workout.reps, 50)
